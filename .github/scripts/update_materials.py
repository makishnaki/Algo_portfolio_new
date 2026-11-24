"""Переносит новые материалы из шаблона курса в репозиторий студента.

Запуск: python3 update_materials.py <папка шаблона> <папка репозитория студента>

Файлы преподавателя заменяются версией из шаблона. Остальные файлы
добавляются только при отсутствии в репозитории студента.
"""
import filecmp
import os
import shutil
import sys

TEACHER_DIRS = ("lectures/", "materials/", "docs/", ".github/scripts/")
TEACHER_FILES = (".gitattributes", ".gitignore", "LICENSE", "requirements.txt")
TEACHER_INDEXES = ("homework/README.md", "practice/README.md", "research/README.md", "exams/README.md")
SKIP_DIRS = (".git/", ".github/workflows/")


def is_teacher_file(relative_path):
    return relative_path.startswith(TEACHER_DIRS) or relative_path in TEACHER_FILES + TEACHER_INDEXES


def template_files(root):
    for directory, directories, files in os.walk(root):
        directories[:] = sorted(
            name
            for name in directories
            if not os.path.relpath(os.path.join(directory, name), root)
            .replace(os.sep, "/")
            .startswith(SKIP_DIRS)
        )
        for name in sorted(files):
            relative_path = os.path.relpath(os.path.join(directory, name), root).replace(os.sep, "/")
            if not relative_path.startswith(SKIP_DIRS):
                yield relative_path


def main(template_root, student_root):
    added, updated = [], []
    for relative_path in template_files(template_root):
        source = os.path.join(template_root, relative_path)
        destination = os.path.join(student_root, relative_path)
        if not os.path.exists(destination):
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            shutil.copy2(source, destination)
            added.append(relative_path)
        elif is_teacher_file(relative_path) and not filecmp.cmp(source, destination, shallow=False):
            shutil.copy2(source, destination)
            updated.append(relative_path)

    if added or updated:
        report = "\n".join(
            [f"Новых файлов: {len(added)}, обновлено: {len(updated)}."]
            + [f"- добавлен `{path}`" for path in added]
            + [f"- обновлён `{path}`" for path in updated]
        )
    else:
        report = "Новых материалов нет."
    print(report)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("## Обновление материалов курса\n\n" + report + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Запуск: python3 update_materials.py <папка шаблона> <папка репозитория студента>")
    main(sys.argv[1], sys.argv[2])
