#! python3
# -*- coding: utf-8 -*-
from os import listdir
from os.path import join
problemPath = join(".", "problems")
problems = tuple(sorted(listdir(path=problemPath), reverse=True))
bannerImg = "https://f.thumbs.redditmedia.com/_23zdeL5L1OqQyIw.png"
bannerUrl = "https://www.reddit.com/r/dailyprogrammer/"
text = []
text.append('[![dailyprogrammer banner](%s "r/dailyprogrammer")](%s)' %
            (bannerImg, bannerUrl))
relHeader = "../master/problems/"
for path in problems:
    pText = []
    date, name = path.rstrip(".py").split(" ", 1)
    relPath = relHeader + path.replace(" ", "%20").replace("#", "%23")
    with open(join(problemPath, path)) as f:
        f.readline()
        f.readline()
        url = f.readline().lstrip("# ")
    pText.append('  * [%s](%s "Problem post at reddit")' % (date, url))
    pText.append("[%s](%s)" % (name, relPath))
    text.append(" __**-**__ ".join(pText))
with open("README.md", "w") as f:
    f.write("\n\n".join(text))
