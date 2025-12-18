import argparse
from lark import Lark
from transformer import ConfigTransformer

def main():
    parser = argparse.ArgumentParser(
        description="Учебный конфигурационный язык"
    )
    parser.add_argument("file", help="Файл конфигурации")
    args = parser.parse_args()

    with open("grammar.lark", encoding="utf-8") as f:
        grammar = f.read()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    parser_lark = Lark(grammar, parser="lalr")
    tree = parser_lark.parse(text)

    transformer = ConfigTransformer()
    result = transformer.transform(tree)

    config = {}
    for item in result:
        if isinstance(item, tuple):
            config[item[0]] = item[1]

    for key, value in config.items():
        print(f"{key} = {value}")

if __name__ == "__main__":
    main()
