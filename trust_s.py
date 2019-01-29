"""
software模块添加新的 x_开头的算法
software模块添加首新人的github和dockerhub账号
"""

from cytomine import Cytomine
from cytomine.models import SoftwareUserRepository
Cytomine.connect("192.168.52.120", "00d8474f-7fd8-4c50-bf8e-79973dcf7bc0", "2e088a54-26ab-4f8e-9bd5-d861479ecbfe")
SoftwareUserRepository(provider="Github", username="zhang-free", docker_username="zhangpenghui", prefix="S_").save()
