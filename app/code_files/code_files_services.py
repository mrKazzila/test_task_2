from datetime import datetime

from django.core.paginator import Paginator


def create_paginator_obj(files, page_number):
    """
    Create a paginator object for the given list of files.

    Args:
        files (list): List of files to be paginated.
        page_number (int): The page number to retrieve.

    Returns:
        Page: The requested page of files.
    """
    paginator = Paginator(files, 8)
    return paginator.get_page(page_number)


def return_old_file_name_if_file_exist(model, owner, file_name):
    """
    Check if a file with the given name exists for the specified owner in the model.

    Args:
        model: The model to query for file existence.
        owner: ID of the owner user.
        file_name: Name of the file to check.

    Returns:
        True if the file exists, False otherwise.
    """
    is_exist_file = model.objects.filter(user=owner, filename__exact=file_name).first()
    return is_exist_file


def delete_file(model, file_pk, user):
    """
    Delete the specified file if it belongs to the given user.

    Args:
        model: The model containing the file to be deleted.
        file_pk: Primary key of the file to be deleted.
        user: The user who owns the file.
    """
    uploaded_file = model.objects.get(pk=file_pk)

    if uploaded_file.user == user:
        uploaded_file.delete()


def file_manager(form, new_file_name, user, old_file):
    """
    Manage file operations based on the presence of an old file.

    Args:
        form: The form object containing file data.
        new_file_name (str): Name of the new file.
        user: The user associated with the file.
        old_file: The old file object to update, if exists.
    """
    is_old_file_name_exist = int(bool(old_file))

    file_operations = {
        0: add_new_file,
        1: update_exist_file,
    }

    file_operations.get(is_old_file_name_exist)(form, new_file_name, user, old_file)


def add_new_file(form, new_file_name, user, old_file=None):
    """
    Add a new file entry to the database.

    Args:
        form: The form object containing file data.
        new_file_name (str): Name of the new file.
        user: The user associated with the file.
        old_file: The old file object, if available.
    """
    new_file = _create_file_odj(
        form_odj=form,
        user=user,
        is_new_status=True,
        filename=new_file_name,
        is_checked_status=False,
    )
    new_file.save()


def update_exist_file(form, new_file_name, user, old_file):
    """
    Update an existing file entry in the database.

    Args:
        form: The form object containing file data.
        new_file_name (str): Name of the new file.
        user: The user associated with the file.
        old_file: The old file object to update.
    """
    new_uploaded_file = _create_file_odj(
        form_odj=form,
        user=user,
        is_new_status=False,
        filename=new_file_name,
        is_checked_status=False,
    )
    new_uploaded_file.uploaded_at = datetime.now()
    old_file.delete()
    new_uploaded_file.save()


def _create_file_odj(form_odj, user, filename, is_new_status, is_checked_status):
    """
    Create a file object from the given form data.

    Args:
        form_obj: The form object containing file data.
        user: The user associated with the file.
        filename (str): Name of the file.
        is_new_status (bool): Indicates if the file is new.
        is_checked_status (bool): Indicates if the file is checked.

    Returns:
        File object: The created file object.
    """
    file_obj = form_odj.save(commit=False)
    file_obj.user = user
    file_obj.is_new = is_new_status
    file_obj.filename = filename
    file_obj.is_checked = is_checked_status

    return file_obj
