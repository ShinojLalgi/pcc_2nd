from admin_module import Admin

me = Admin('shinoj', 'lagi')
me.privileges.adminprivileges = ['can edit posts', 'can remove participants']
me.privileges.showprivileges()