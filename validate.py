import argparse
import pathlib
import sys

import frontmatter


def get_doc_type(path: pathlib.Path) -> str:
    """Determine the document type from the file path."""
    return path.parent.name


def get_template_path(doc_type: str) -> pathlib.Path:
    """Get the path to the template for the given document type."""
    doc_type_mapping = {
        "policies": "policy",
        "standards": "standard",
        "processes": "process",
        "guidance": "guidance",
    }
    template_doc_type = doc_type_mapping.get(doc_type, doc_type)
    return pathlib.Path(f"templates/{template_doc_type}-template.md")


def validate_frontmatter(doc: frontmatter.Post, template: frontmatter.Post) -> list[str]:
    """Validate the document's frontmatter against the template."""
    errors = []
    for key in template.keys():
        if key not in doc.keys():
            errors.append(f"Missing frontmatter key: {key}")
    return errors


def validate_headings(doc_content: str, template_content: str) -> list[str]:
    """Validate the document's headings against the template."""
    errors = []
    doc_headings = {line for line in doc_content.splitlines() if line.startswith("#")}
    template_headings = {
        line for line in template_content.splitlines() if line.startswith("#")
    }
    for heading in template_headings:
        if heading not in doc_headings:
            errors.append(f"Missing heading: {heading}")
    return errors


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Validate a document against a template.")
    parser.add_argument("paths", nargs="+", type=pathlib.Path, help="Paths to the documents to validate.")
    args = parser.parse_args()

    error_found = False
    for path in args.paths:
        if not path.exists():
            print(f"Error: File not found: {path}", file=sys.stderr)
            error_found = True
            continue

        doc_type = get_doc_type(path)
        template_path = get_template_path(doc_type)

        if not template_path.exists():
            print(f"Warning: No template found for document type '{doc_type}'", file=sys.stderr)
            continue

        doc = frontmatter.load(path)
        template = frontmatter.load(template_path)

        errors = []
        errors.extend(validate_frontmatter(doc, template))
        errors.extend(validate_headings(doc.content, template.content))

        if errors:
            error_found = True
            print(f"Validation errors for {path}:", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)

    if error_found:
        sys.exit(1)


if __name__ == "__main__":
    main()
