def select_one_per_category(messages, categories):
    selected = []
    for cat in categories:
        for i, msg in enumerate(messages):
            if msg.get('category') == cat:
                selected.append(msg)
                messages.pop(i) 
                break
    return selected