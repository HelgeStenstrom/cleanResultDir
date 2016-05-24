import cleaner as c
import unittest
import sys
import io


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def testParser(self):
        parser = c.parse_args(['someDirectory'])
        self.assertEqual(parser.resultRoot, 'someDirectory')

    def testTooManyArgs(self):
        self.assertRaises(SystemExit, c.parse_args, ['hej', 'hopp'])
        # also too few arguments
        self.assertRaises(SystemExit, c.parse_args, [])

class MoreTests(unittest.TestCase):
    def testNonExisting(self):
        self.assertRaises(NotADirectoryError, c.checkIsRoot, '/nonexisting')

class RunDirTests(unittest.TestCase):
    def testHasFilesOnly(self):
        'A results directory has a few results files, but no sub directory.'
        self.assertFalse(c.hasFilesOnly('/'))

# I slutändan vill jag att mitt program ska rensa bland filerna. Vägen
# dit kan gå via att ändra namn på mappar som ska rensas bort.
# Jag vill komma dit genom att skapa funktioner som kan testas
# oberoende av något filsystem.

# Saker att filtrera på:
# - att mappen har rätt nivåer.
# - Att nödvändiga filer finns där, annars är mappen värdelös.

# Rätt nivåer är:
# 1. Roten, den som anges i OneTE GUI
# 2. Nivå med mappar som namnges enligt TOL
# 3. Nivå med mappar som har namn med tidsstämpel
# 4. Nivå med filer, men inga undermappar.

# Användbara funktioner
# glob.glob(root + '/*/*/*')
# returnerar, tror jag, filerna, och ska inte returnera några mappar,
# om det är rätt typ av resultatmapp.
# Se
# http://stackoverflow.com/questions/7159607/list-directories-with-a-specified-depth-in-python

# Problemet just nu, är att jag inte kan komma på någon användbar
# funktion att skriva, som inte antingen är beroende av befintliga
# filer (vilket kan simuleras, men det är jobbigt), eller har
# sideffekter (vilka är önskvärda, men inte för testning).

# re.search('([0-9]+_[0-9]+_[0-9]+-LPA_109_332_1-[0-9]{1,3})', '2_152_82-LPA_109_332_1-906').group(0)
# d = '2_152_82-LPA_109_332_1-906'
# re.search('(\d{1,3}_\d{1,3}-LPA_109_332_1-\d{1,3})', d).group(0)
# re.search('(\d_152_82-LPA_109_332_1-\d{1,3})', d).group(0)

if __name__ == '__main__':
    unittest.main()
