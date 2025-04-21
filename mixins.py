class PersistMixin:
    @staticmethod
    def save(object_to_save: dict, list_of_objects: list)-> dict:
        """
        Save object to list of objects
        :param object_to_save: the objects to save
        :param list_of_objects: the list of objects to save to
        :return: dict
        """
        for obj in list_of_objects:
            if obj["id"] == object_to_save["id"]:
                obj.update(object_to_save)
                return obj
        list_of_objects.append(object_to_save)
        return object_to_save