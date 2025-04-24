class CustomString:
    def __init__(self, skill_name):
        self.skill_name = skill_name


    def effect_tooltip(self, tt_ext):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        effects = (
            f'effect: .name "{self.skill_name}_TooltipEffect{tt_ext}" .target "performer" '
            f'.skill_instant true .buff_ids "{self.skill_name}_Tooltip{tt_ext}" '
            f'.duration 3 .on_hit false .on_miss false'
        )
        return effects

    def buff_tooltip(self, tt_ext):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        data = {
            "id": f"{self.skill_name}_Tooltip{tt_ext}",
            "stat_type": "upgrade_discount",
            "stat_sub_type": f"Loc_{self.skill_name}_Tooltip{tt_ext}",
            "amount": 5,
            "remove_if_not_active": False,
            "rule_type": "always",
            "is_false_rule": False,
            "rule_data": {
                "float": 0,
                "string": ""
            }
        }

        return data

    def loc_tooltip(self, tt_ext, description):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        loc = f'<entry id="buff_stat_tooltip_upgrade_discount_Loc_{self.skill_name}_Tooltip{tt_ext}"><![CDATA[{description}]]></entry>\n'
        return loc
    
