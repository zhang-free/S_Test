from cytomine import Cytomine
from cytomine.utilities.descriptor_reader import read_descriptor
with Cytomine("192.168.52.120", "00d8474f-7fd8-4c50-bf8e-79973dcf7bc0", "2e088a54-26ab-4f8e-9bd5-d861479ecbfe") as c:
    software = read_descriptor("descriptor.json")
    print("Not executable software created with ID {}".format(software.id))