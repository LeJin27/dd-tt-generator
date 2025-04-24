import json
import os
import shutil
from datetime import datetime
from CustomString import CustomString
import xml.etree.ElementTree as ET
import xml.dom.minidom


class Generator:
    def __init__(self):
        self.custom_string = CustomString()

    def backup_file(self, file_name):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        backup_dir = "backup"
        os.makedirs(backup_dir, exist_ok=True)

        base = os.path.splitext(os.path.basename(file_name))[0]
        backup_path = os.path.join(backup_dir, f"{base}_backup_{timestamp}.txt")

        shutil.copy(file_name, backup_path)



    def effect_file(self, skill_name, tt_ext, file_name):
        line_to_add = self.custom_string.effect_tooltip(skill_name, tt_ext)
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(line_to_add + '\n')

    def buff_file(self, skill_name, tt_ext, file_name):
        self.backup_file(file_name)


        with open(file_name, 'r') as file:
            data = json.load(file)

        buffsList = data['buffs']
        buffsList.append(self.custom_string.buff_tooltip(skill_name, tt_ext))

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)


    def loc_file(self, skill_name, tt_ext, description, file_name):
        self.backup_file(file_name)

        string_to_add = self.custom_string.loc_tooltip(skill_name, tt_ext, description)

        tree = ET.parse(file_name)
        tree_root = tree.getroot()
        tree_lang_elem = tree_root.find(".//language[@id='english']")

        appended_entry = ET.fromstring(string_to_add)
        tree_lang_elem.append(appended_entry)

        xml_to_string = ET.tostring(tree_root, encoding="utf-8")
        xml_parsed_string = xml.dom.minidom.parseString(xml_to_string)

        dom_string = xml_parsed_string.toprettyxml()
        dom_string = os.linesep.join([s for s in dom_string.splitlines() if s.strip()])
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(dom_string)  


def main(): 
    test = Generator()
    test.loc_file('skill_name', '1A', 'cooliosis', 'swap_sb.string_table.xml')

if __name__ == "__main__":
    main()