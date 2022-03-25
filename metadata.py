import datetime
import json
import os

from metadata_model import AttributeModel, MetadataModel

IMAGES_BASE_URL = os.environ["IMAGES_BASE_URL"]
PROJECT_NAME = "HiddenBeauty"


def generate_metadata():
    timestamp = datetime.datetime.utcnow().timestamp()
    with open("./all-traits.json") as f:
        data = json.load(f)
        for row in data:
            token_id = row["tokenId"]
            token = MetadataModel(
                image=f"{IMAGES_BASE_URL}{token_id}.png",
                name=f"{PROJECT_NAME} #{token_id}",
                description="""A collection of 10.000 art objects "My beauty is hidden from you". We say "I don't have to show you my beauty". "My eye is where I want it," says Picasso. The eye is something that still needs to be released.""",
                edition=token_id,
                date=int(timestamp),
                attributes=[
                    AttributeModel(trait_type=key, value=value)
                    for key, value in row.items()
                    if key != "path"
                ],
            )

            with open("./metadata/" + str(token_id), "w") as outfile:
                json.dump(token.dict(), outfile, indent=4)


if __name__ == "__main__":
    generate_metadata()
