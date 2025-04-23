import json


class Generator:
    def __init__(self, skill_name):
        self.skill_name = skill_name

    def append_effect(self, file_path, line_to_add):
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(line_to_add + '\n')

    def effect_tooltip(self, count):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        effects = (
            f'effect: .name "{self.skill_name}_TooltipEffect{count}" .target "performer" '
            f'.skill_instant true .buff_ids "{self.skill_name}_Tooltip{count}" '
            f'.duration 3 .on_hit false .on_miss false'
        )
        return effects

    def buff_tooltip(self, count):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        data = {
            "id": f"{self.skill_name}_Tooltip{count}",
            "stat_type": "upgrade_discount",
            "stat_sub_type": f"Loc_{self.skill_name}_Tooltip{count}",
            "amount": 5,
            "remove_if_not_active": False,
            "rule_type": "always",
            "is_false_rule": False,
            "rule_data": {
                "float": 0,
                "string": ""
            }
        }

        json_data = json.dumps(data, indent=2)
        return json_data

    def loc_tooltip(self, count, description):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        loc = f'<entry id="buff_stat_tooltip_upgrade_discount_Loc_{self.skill_name}_Tooltip{count}"><![CDATA[{description}]]></entry>'
        print(loc)




test = Generator('LashGift')
# tooltip_effects = test.effects_tooltip('1A')

test.loc_tooltip('1A', 'cooldown')
