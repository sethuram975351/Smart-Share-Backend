from AccessManagementService import databaseInstance

class ObjectRelationalModel:

    class Owner(databaseInstance.Model):
        id = databaseInstance.Column(databaseInstance.Integer, primary_key=True)
        name = databaseInstance.Column(databaseInstance.Text)
        files = databaseInstance.relationship('File', lazy=True)

    class File(databaseInstance.Model):
        id = databaseInstance.Column(databaseInstance.Integer, primary_key=True)
        name = databaseInstance.Column(databaseInstance.Text)
        ownerId = databaseInstance.Column(databaseInstance.Integer, databaseInstance.ForeignKey('owner.id'),
                                          name="owner_id")
        owner = databaseInstance.relationship("Owner")
        users = databaseInstance.relationship("FileUserAccess", backref="file", cascade="save-update, merge, "
                                                                                        "delete, delete-orphan")

    class FileUserAccess(databaseInstance.Model):
        fileId = databaseInstance.Column(databaseInstance.Integer, databaseInstance.ForeignKey('file.id'),
                                         primary_key=True, name="file_id")
        userId = databaseInstance.Column(databaseInstance.Integer, databaseInstance.ForeignKey('user.id'),
                                         primary_key=True, name="user_id")
        accessId = databaseInstance.Column(databaseInstance.Integer,
                                           databaseInstance.ForeignKey('permissions_assigned.id'), name="access_id")
        accessGiven = databaseInstance.relationship('PermissionsAssigned')

    class User(databaseInstance.Model):
        id = databaseInstance.Column(databaseInstance.Integer, primary_key=True)
        name = databaseInstance.Column(databaseInstance.Text)
        files = databaseInstance.relationship("FileUserAccess", backref="user")

    class PermissionsAssigned(databaseInstance.Model):
        id = databaseInstance.Column(databaseInstance.Integer, primary_key=True)
        read = databaseInstance.Column(databaseInstance.Boolean)
        write = databaseInstance.Column(databaseInstance.Boolean)
        delete = databaseInstance.Column(databaseInstance.Boolean)

        def __repr__(self):
            return '<PermissionsAssigned %r %r %r>' % (
                self.read, self.write, self.delete)

    class AccessRequest(databaseInstance.Model):
        id = databaseInstance.Column(databaseInstance.Integer, primary_key=True)
        file = databaseInstance.Column(databaseInstance.Text)
        ownerOfFile = databaseInstance.Column(databaseInstance.Text, name='owner_of_file')
        userName = databaseInstance.Column(databaseInstance.Text, name='user_name')
        accessType = databaseInstance.Column(databaseInstance.Text, name='access_type')
        statusOfRequest = databaseInstance.Column(databaseInstance.Text, name='status_of_request')

        def __repr__(self):
            return '<AccessRequest %r %r %r %r %r %r>' % (
                self.id, self.file, self.ownerOfFile, self.userName, self.accessType, self.statusOfRequest)
