def setup():
    name = "P2-Platypodes"
    source = {"name": name}  # source dictionary used to define certain Jinja variables

    project1 = "Frontend"  # frontend links
    projlinks1 = [
        Link("GitHub", "https://github.com/aymankazi9/P2-Platypodes/tree/main/templates")
    ]

    project2 = "Backend"  # backend links
    projlinks2 = [
        Link("GitHub", "https://github.com/aymankazi9/P2-Platypodes/blob/main/stats.py")
    ]

    # Project Objects
    proj1 = Model(project1, projlinks1)

    proj2 = Model(project2, projlinks2)
    # HTML Data
    projects = Models(source, [proj1, proj2])
    return projects

class Faq():
    def __init__(self):
        self._q1 = "1. What is global warming?"

    @property
    def q1(self):
        return self._q1

    @q1.setter
    def q1(self, value):
        self._q1 = value


# class for button label and href
class Link():
    # href is linked to button label
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href


# Model data class contain model name and links (Link class objects)
class Model():
    # model data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


# Models class contains person (owner) and multiple projects (Models class objects)
class Models():
    # HTML data with source and models
    def __init__(self, source, model):
        self.source = source
        self.model = model

    # source data
    def get_source(self):
        return self.source

    # projects data
    def get_model(self):
        return self.model