# -*- coding: utf-8 -*-

def generate_xml_output(result):
    # Generate XML output

    from xml.dom.minidom import parse, parseString

    dom = parseString('<items></items>')
    items = dom.childNodes[0]

    for key, value in result.items():
        item = dom.createElement('item')
        item.setAttribute('arg', value)
        items.appendChild(item)

        title = dom.createElement('title')
        title.appendChild(dom.createTextNode(key))
        item.appendChild(title)

        subtitle = dom.createElement('subtitle')
        subtitle.appendChild(dom.createTextNode(value))
        item.appendChild(subtitle)

        icon = dom.createElement('icon')
        icon.appendChild(dom.createTextNode('icon.png'))
        item.appendChild(icon)

    print(dom.toxml())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Hash Strings')
    parser.add_argument('--value', help='value')
    parser.add_argument('--md5', help='md5', action="store_true")
    parser.add_argument('--sha1', help='sha1', action="store_true")
    parser.add_argument('--sha256', help='sha256', action="store_true")
    parser.add_argument('--sha512', help='sha256', action="store_true")
    parse_args = parser.parse_args()

    value = parse_args.value
    import hashlib

    if parse_args.md5:
        generate_xml_output({'MD5': hashlib.md5(value).hexdigest()})
    elif parse_args.sha1:
        generate_xml_output({'SHA1': hashlib.sha1(value).hexdigest()})
    elif parse_args.sha256:
        generate_xml_output({'SHA256': hashlib.sha256(value).hexdigest()})
    elif parse_args.sha512:
        generate_xml_output({'SHA512': hashlib.sha512(value).hexdigest()})
