class Club():

    def __init__(self, club_name, max_members):
        self.club_name = club_name
        self.max_members = max_members
        self.members_list = []

    def add_member(self, name):
        if len(self.members_list) < self.max_members:
            self.members_list.append(name)
            print('OK.', name, 'has been added to the', self.club_name, 'club')
        else:
            print('Sorry, but we cannot add', name, 'to the', self.club_name, 'club.')
            print('This club already has the maximum of', self.max_members, 'members.')

    def report(self):
        print()
        print('Here are the', len(self.members_list), 'members of the', self.club_name, 'club:')
        for name in self.members_list:
            print('   ' + name)
        print()

