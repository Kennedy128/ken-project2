from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.user_victor = User(username = 'kennedy',password = 'kennedy', email = 'kennedymbithi12@gmail.com')
    self.new_pitch = Pitch(id=1,title='Test',description='This is a test pitch',category="interview",user = self.user_kennedy,upvotes=0,downvotes=0)
    self.new_comment = Comment(id=1, content='Test comment',user=self.user_kennedy,pitch=self.new_pitch)


  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.content,'Test comment')
    self.assertEquals(self.new_comment.user,self.user_kennedy)
    self.assertEquals(self.new_comment.pitch,self.new_pitch)