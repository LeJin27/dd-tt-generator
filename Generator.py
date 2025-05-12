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



    def effect_file(self, skill_name, file_name):
        self.backup_file(file_name)
        line_to_add = self.custom_string.effect_tooltip(skill_name)
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write('\n' + line_to_add + '\n')

    def buff_file(self, skill_name, file_name):
        self.backup_file(file_name)


        with open(file_name, 'r') as file:
            data = json.load(file)

        buffsList = data['buffs']
        buffsList.append(self.custom_string.buff_tooltip(skill_name))

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def loc_file(self, skill_name, description, file_name):
        self.backup_file(file_name)
    
        # Load with minidom instead of ElementTree
        with open(file_name, 'r', encoding='utf-8') as f:
            dom = xml.dom.minidom.parse(f)
    
        language_node = dom.getElementsByTagName('language')
        english_lang = None
        for lang in language_node:
            if lang.getAttribute('id') == 'english':
                english_lang = lang
                break
            
        if not english_lang:
            raise ValueError("No <language id='english'> found.")
    
        entry = dom.createElement('entry')
        entry.setAttribute('id', f'buff_stat_tooltip_upgrade_discount_{skill_name}')
    
        cdata = dom.createCDATASection(description)
        entry.appendChild(cdata)
    
        english_lang.appendChild(entry)
    
        with open(file_name, 'w', encoding='utf-8') as f:
            dom_string = dom.toprettyxml(indent="  ")
            f.write(dom_string)



def main(): 
    test = Generator()
    test.loc_file('skill_name', 'cooliosis', 'swap_sb.string_table.xml')

if __name__ == "__main__":
    main()