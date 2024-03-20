color_map = {
    "O": "#FFFFFF",  # White (Outside of a named entity)
    "MISC": "#FFA07A",  # Light Salmon (Beginning of a miscellaneous entity right after another miscellaneous entity)
    "PER": "#7B68EE",  # Medium Slate Blue (Beginning of a person’s name right after another person’s name)
    "ORG": "#20B2AA",  # Light Sea Green (Beginning of an organization right after another organization)
    "LOC": "#87CEEB",  # Sky Blue (Beginning of a location right after another location)
}


def format_ner_text(text:str, ner_result:dict):
    formatted_text = ""
    last_end = 0
    for result in ner_result:
        start = result["start"]
        end = result["end"]
        entity = result["word"]
        entity_type = result["entity_group"]
        formatted_text += text[last_end:start]
        
        # print(f"entity_type: {entity_type}" )

        color = color_map.get(entity_type, "#FFFFFF")  # Default to white if no color found
        formatted_text += f"""<span style='background-color: {color};'>{entity} </span>  <span style="font-family: Consolas; font-size: 13px;background-color: {color};">[{entity_type.lower()}]</span>  """

        last_end = end
        
    formatted_text += text[last_end:]
    return formatted_text