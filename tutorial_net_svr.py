from flask import Flask
from flask_cors import CORS
import pymongo


app = Flask(__name__)


users = [
    {"username": "nik"},
    {"username": "mitt"}
]
courses = {
    "c1": {
        "name": "Circuit Design"
    }
}
topics = {
    "t1": {
        "name": "Creating components",
        "courses": ["c1"],
        "artifacts": ["a1", "a2"]
    }
}
artifacts = {
    "a1": {
        "topics": ["t1"],
        "mastery_ct": 1,
        "learn_index": 0,
        "type": "text",
        "confirmation": False,
        "timeout": 7,
        "text": "To create a component, click the \"+\" button and choose the appropriate icon."
    },
    "a2": {
        "topics": ["t1"],
        "mastery_ct": 1,
        "learn_index": 1,
        "type": "text",
        "confirmation": False,
        "timeout": 7,
        "text": "You can hover over each icon to get more information about the component they represent."
    },
    "a3": {
        "topics": ["t1"],
        "mastery_ct": 1,
        "learn_index": 0,
        "type": "interactive",
        "sub_artifacts": ["a1", "a2"],
        "path": "components/labs/a3"
    }
}
completion = [
    # {"user": "nik", "artifact": "a_1", "ts": 0, "display_ct": 0, "pass_ct": 0, "fail_ct": 0}
]


@app.route("/users", methods=["GET"])
def get_users():
    return users


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2149)
