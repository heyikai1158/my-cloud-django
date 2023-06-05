# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    from_id = models.IntegerField(db_comment='发起人')
    receive_id = models.IntegerField(db_comment='接收人')
    create_time = models.DateTimeField(db_comment='发起时间')
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat'


class ChatRecords(models.Model):
    attribute_id = models.IntegerField(db_comment='归属于哪个聊天表')
    send_by = models.IntegerField(db_comment='发送人ID')
    content = models.TextField(db_comment='消息内容')
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat_records'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class File(models.Model):
    name = models.CharField(max_length=255, db_comment='文件名')
    type = models.CharField(max_length=255, blank=True, null=True, db_comment='文件类型/拓展名')
    size = models.FloatField(db_comment='文件大小(MB)')
    dir_id = models.IntegerField(blank=True, null=True, db_comment='所属文件夹(null为根目录)')
    user_id = models.IntegerField(db_comment='所属用户')
    upload_time = models.DateTimeField(db_comment='上传时间')
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file'


class FileRecords(models.Model):
    is_from_share = models.IntegerField(db_comment='源于分享')
    time = models.DateTimeField(db_comment='操作时间')
    file_id = models.IntegerField(db_comment='文件ID')
    user_id = models.IntegerField(db_comment='操作人ID')

    class Meta:
        managed = False
        db_table = 'file_records'


class Folder(models.Model):
    parent_dir = models.IntegerField(blank=True, null=True, db_comment='父级ID')
    dir = models.CharField(max_length=255, db_comment='文件夹名称')
    user_id = models.IntegerField(db_comment='所属用户')
    is_del = models.IntegerField(db_comment='删除则为1，默认为0')

    class Meta:
        managed = False
        db_table = 'folder'


class Share(models.Model):
    create_time = models.DateTimeField(db_comment='创建时间')
    expire_time = models.DateTimeField(blank=True, null=True, db_comment='过期时间(null为永不过期)')
    file_id = models.IntegerField(db_comment='文件ID')
    user_id = models.IntegerField(db_comment='分享人ID')
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'share'


class User(models.Model):
    name = models.CharField(max_length=255, db_comment='用户名')
    passwd = models.CharField(max_length=255, db_comment='密码')
    space_size = models.FloatField(db_comment='网盘空间')
    level_vip = models.IntegerField(db_comment='会员等级')
    online_status = models.IntegerField(db_comment='在线状态')

    class Meta:
        managed = False
        db_table = 'user'
