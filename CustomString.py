class CustomString:

    def effect_tooltip(self, skill_name):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        effects = (
            f'effect: .name "{skill_name}" .target "performer" '
            f'.skill_instant true .buff_ids "{skill_name}" '
            f'.duration 3 .on_hit false .on_miss false'
        )
        return effects

    def buff_tooltip(self, skill_name):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        data = {
            "id": f"{skill_name}",
            "stat_type": "upgrade_discount",
            "stat_sub_type": f"{skill_name}",
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

    def loc_tooltip(self, skill_name, description):
        """
        Generates a tooltip effect string for the given skill.

        Args:
            count (int): The number of tooltip effects to generate (though not used in the current implementation, it might be useful in future modifications).
        Returns:
            str: A formatted string representing the tooltip effect for the skill.
        """
        loc = f'<entry id="buff_stat_tooltip_upgrade_discount_{skill_name}"><![CDATA[{description}]]></entry>\n'
        return loc
    
