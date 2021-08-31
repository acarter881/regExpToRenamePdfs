import re
import os
from thisHoldsHtml import HTML

class ParseAndRename:
    def __init__(self) -> None:
        self.docList = []
        self.bigData = []

    def __repr__(self) -> str:
        return 'This class helps to parse HTML and rename PDF files.'

    def findMatches(self):
        self.pdfs = re.findall(pattern=r'\w+\.pdf', string=HTML)
        self.sapDocs = re.findall(pattern=r'>((51|17)\d{8})<', string=HTML)
        return self.pdfs, self.sapDocs

    def createSapDocList(self):
        for docTuple in self.sapDocs:
            self.docList.append(docTuple[0])

    def removeDuplicatesMaintainOrder(self, seq):
        self.seen = set()
        self.seen_add = self.seen.add
        return [x for x in seq if not (x in self.seen or self.seen_add(x))]

    def finalPdfs(self):
        self.finalList = self.removeDuplicatesMaintainOrder(self.pdfs)
        return self.finalList

    def finalDict(self):
        for i in range(len(self.finalList)):
            self.bigData.append((self.finalList[i], self.docList[i]))
        self.bigData = dict(self.bigData)
        return self.bigData

    def changeDir(self):
        os.chdir(r'C:\Users\REDACTED\Desktop\Presentation\pdfDoc_1')

    def rename(self):
        for filename in os.listdir(r'C:\Users\REDACTED\Desktop\Presentation\pdfDoc_1'):
            if filename.endswith('.pdf'):
                if filename in self.bigData:
                    os.rename(filename, self.bigData[filename] + '.pdf')

# Instantiate the class and run the necessary functions
c = ParseAndRename()
c.findMatches()
c.createSapDocList()
c.finalPdfs()
c.finalDict()
c.changeDir()
c.rename()
