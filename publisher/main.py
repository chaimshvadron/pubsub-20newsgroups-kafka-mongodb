from fastapi import FastAPI
from data_loader import load_messages
from category_selector import select_one_per_category
from producer import send_messages, TOPICS

app = FastAPI()

interesting_categories = [
    'alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos',
    'rec.motorcycles', 'rec.sport.baseball'
]
not_interesting_categories = [
    'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space',
    'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast',
    'talk.politics.misc', 'talk.religion.misc'
]

@app.get("/publish")
def publish_messages():
    interesting_msgs = load_messages("data/newsgroups_interesting.json")
    not_interesting_msgs = load_messages("data/newsgroups_not_interesting.json")
    selected_interesting = select_one_per_category(interesting_msgs, interesting_categories)
    selected_not_interesting = select_one_per_category(not_interesting_msgs, not_interesting_categories)

    send_messages(TOPICS["interesting"], selected_interesting)
    send_messages(TOPICS["not_interesting"], selected_not_interesting)

    return {
        "status": "published",
        "count_interesting": len(selected_interesting),
        "count_not_interesting": len(selected_not_interesting)
    }