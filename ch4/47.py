# Build Order
# all of a projects dependencies must be built before the project

def build_order(projects, dependencies):
    order = []
    #find projects with no dependencies
    for project in projects:
        if project not in dependencies:
            order.append(project)
    #keep clearing dependencies
    for project in order:
        for key, value in dependencies.items():
            if project in value:
                value.remove(project) # try to remove dependency
                if len(value) == 0:
                    order.append(key)
    print(order)


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = {'a': ['d'],
        'f': ['a', 'b'],
        'b': ['d'],
        'd': ['c']}
    build_order(projects, dependencies)
