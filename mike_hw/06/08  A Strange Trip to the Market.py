# https://www.codewars.com/kata/55ccdf1512938ce3ac000056
import re
from helper import test


def is_lock_ness_monster(string):
    return bool(re.search("tree fiddy|3\.50|three fifty", string))


# проверка
test.assert_equals(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"), True)
test.assert_equals(is_lock_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"), True)
test.assert_equals(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"), True)
test.assert_equals(is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."), False)
test.assert_equals(is_lock_ness_monster("I will absolutely, positively, never give that darn Lock Ness Monster any of my three dollars and fifty cents"), False)
test.assert_equals(is_lock_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."), False)
test.assert_equals(is_lock_ness_monster("Hello, I come from the year 3150 to bring you good news!"), False)
test.assert_equals(is_lock_ness_monster("By 'tree fiddy' I mean 'three fifty'"), True)
test.assert_equals(is_lock_ness_monster("I will be at the office by 3:50 or maybe a bit earlier, but definitely not before 3, to discuss with 50 clients"), False)
test.assert_equals(is_lock_ness_monster(""), False)

