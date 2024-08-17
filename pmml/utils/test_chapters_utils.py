import chapters_utils

def test_get_chapter_count_when_no_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":467},"sortOrder":0,"id":120,"storyBookParagraphs":[]},{"image":{"id":468},"sortOrder":1,"id":121,"storyBookParagraphs":[]},{"image":{"id":469},"sortOrder":2,"id":122,"storyBookParagraphs":[]},{"image":{"id":470},"sortOrder":3,"id":123,"storyBookParagraphs":[]},{"image":{"id":471},"sortOrder":4,"id":124,"storyBookParagraphs":[]},{"image":{"id":472},"sortOrder":5,"id":125,"storyBookParagraphs":[]},{"image":{"id":473},"sortOrder":6,"id":126,"storyBookParagraphs":[]},{"image":{"id":474},"sortOrder":7,"id":127,"storyBookParagraphs":[]},{"image":{"id":475},"sortOrder":8,"id":128,"storyBookParagraphs":[]},{"image":{"id":476},"sortOrder":9,"id":129,"storyBookParagraphs":[]},{"image":{"id":477},"sortOrder":10,"id":130,"storyBookParagraphs":[]},{"image":{"id":478},"sortOrder":11,"id":131,"storyBookParagraphs":[]},{"image":{"id":479},"sortOrder":12,"id":132,"storyBookParagraphs":[]},{"image":{"id":480},"sortOrder":13,"id":133,"storyBookParagraphs":[]},{"image":{"id":481},"sortOrder":14,"id":134,"storyBookParagraphs":[]},{"image":{"id":482},"sortOrder":15,"id":135,"storyBookParagraphs":[]},{"image":{"id":483},"sortOrder":16,"id":136,"storyBookParagraphs":[]},{"image":{"id":484},"sortOrder":17,"id":137,"storyBookParagraphs":[]},{"image":{"id":485},"sortOrder":18,"id":138,"storyBookParagraphs":[]},{"image":{"id":486},"sortOrder":19,"id":139,"storyBookParagraphs":[]},{"image":{"id":487},"sortOrder":20,"id":140,"storyBookParagraphs":[]},{"image":{"id":488},"sortOrder":21,"id":141,"storyBookParagraphs":[]},{"image":{"id":489},"sortOrder":22,"id":142,"storyBookParagraphs":[]},{"image":{"id":490},"sortOrder":23,"id":143,"storyBookParagraphs":[]},{"image":{"id":491},"sortOrder":24,"id":144,"storyBookParagraphs":[]},{"image":{"id":492},"sortOrder":25,"id":145,"storyBookParagraphs":[]},{"image":{"id":493},"sortOrder":26,"id":146,"storyBookParagraphs":[]}]

    # Extract the number of chapters
    chapter_count = chapters_utils.get_chapter_count(chapters_json)

    assert chapter_count == 27

def test_get_chapter_count_when_single_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":447},"sortOrder":0,"id":99,"storyBookParagraphs":[{"originalText":"Earth is the planet that we live on. Currently no other planet is known to contain life.","sortOrder":0,"id":142}]},{"image":{"id":448},"sortOrder":1,"id":100,"storyBookParagraphs":[{"originalText":"The Earth is in danger because of global warming. Global warming is caused by too much carbon dioxide in the atmosphere. Carbon dioxide is a gas which traps heat in the Earth. Without it Earth\'s heat would flow out and Earth would freeze.","sortOrder":0,"id":143}]},{"image":{"id":449},"sortOrder":2,"id":101,"storyBookParagraphs":[{"originalText":"The cars we drive create lots of carbon dioxide. We should walk more or ride a bicycle.","sortOrder":0,"id":144}]}]

    # Extract the number of chapters
    chapter_count = chapters_utils.get_chapter_count(chapters_json)

    assert chapter_count == 3

def test_get_chapter_count_when_multiple_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":529},"sortOrder":0,"id":180,"storyBookParagraphs":[{"originalText":"One day, in a sleepy village with no electricity, the Electricity Department decided to put up electricity poles.","sortOrder":0,"id":219},{"originalText":"The villagers were excited.","sortOrder":1,"id":220}]},{"image":{"id":530},"sortOrder":1,"id":181,"storyBookParagraphs":[{"originalText":"Every day, a big pit was dug out for each pole.","sortOrder":0,"id":221},{"originalText":"The entire village would gather and watch.","sortOrder":1,"id":222}]},{"image":{"id":531},"sortOrder":2,"id":182,"storyBookParagraphs":[{"originalText":"Ropes were used to pull up the poles. The villagers helped lift the poles into the pits.","sortOrder":0,"id":223},{"originalText":"Even the kids pulled the ropes with all their might. \"HAYYIIISHHHHAAAAAA!\"","sortOrder":1,"id":224}]},{"image":{"id":532},"sortOrder":3,"id":183,"storyBookParagraphs":[{"originalText":"Once the poles were up, the Electricity Department team vanished.","sortOrder":0,"id":225},{"originalText":"Every day, the villagers would wait for them to come back and finish their work. All they could talk about was how excited they were to get electricity.","sortOrder":1,"id":226}]},{"image":{"id":533},"sortOrder":4,"id":184,"storyBookParagraphs":[]},{"image":{"id":534},"sortOrder":5,"id":185,"storyBookParagraphs":[{"originalText":"The villagers began climbing up the poles. The poles gave them a perfect view of their surroundings and far away villages.","sortOrder":0,"id":227},{"originalText":"Days passed, with no sign of the Electricity Department team.","sortOrder":1,"id":229}]},{"image":{"id":535},"sortOrder":6,"id":186,"storyBookParagraphs":[{"originalText":"One evening, a little child took a lantern from her house.","sortOrder":0,"id":231},{"originalText":"She climbed up one of the poles and hung the lantern on top.","sortOrder":1,"id":232}]},{"image":{"id":536},"sortOrder":7,"id":187,"storyBookParagraphs":[{"originalText":"Everyone noticed the lovely bright lantern on top of the pole.","sortOrder":0,"id":233}]},{"image":{"id":537},"sortOrder":8,"id":188,"storyBookParagraphs":[]},{"image":{"id":538},"sortOrder":9,"id":189,"storyBookParagraphs":[{"originalText":"The next evening, the villagers hung lanterns from all five poles.","sortOrder":0,"id":234},{"originalText":"Every day, lanterns were taken down, refueled, and hung back up again.","sortOrder":1,"id":235},{"originalText":"The villagers made a game of it and had lots of fun.","sortOrder":2,"id":236}]},{"image":{"id":539},"sortOrder":10,"id":190,"storyBookParagraphs":[{"originalText":"Then, even without electricity, the nearby villages could spot this little village from afar at night.","sortOrder":0,"id":237},{"originalText":"They began calling it \"The Village of Five Poles.\"","sortOrder":1,"id":240}]},{"image":{"id":540},"sortOrder":11,"id":191,"storyBookParagraphs":[]}]

    # Extract the number of chapters
    chapter_count = chapters_utils.get_chapter_count(chapters_json)

    assert chapter_count == 12

def test_get_paragraph_count_when_no_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":467},"sortOrder":0,"id":120,"storyBookParagraphs":[]},{"image":{"id":468},"sortOrder":1,"id":121,"storyBookParagraphs":[]},{"image":{"id":469},"sortOrder":2,"id":122,"storyBookParagraphs":[]},{"image":{"id":470},"sortOrder":3,"id":123,"storyBookParagraphs":[]},{"image":{"id":471},"sortOrder":4,"id":124,"storyBookParagraphs":[]},{"image":{"id":472},"sortOrder":5,"id":125,"storyBookParagraphs":[]},{"image":{"id":473},"sortOrder":6,"id":126,"storyBookParagraphs":[]},{"image":{"id":474},"sortOrder":7,"id":127,"storyBookParagraphs":[]},{"image":{"id":475},"sortOrder":8,"id":128,"storyBookParagraphs":[]},{"image":{"id":476},"sortOrder":9,"id":129,"storyBookParagraphs":[]},{"image":{"id":477},"sortOrder":10,"id":130,"storyBookParagraphs":[]},{"image":{"id":478},"sortOrder":11,"id":131,"storyBookParagraphs":[]},{"image":{"id":479},"sortOrder":12,"id":132,"storyBookParagraphs":[]},{"image":{"id":480},"sortOrder":13,"id":133,"storyBookParagraphs":[]},{"image":{"id":481},"sortOrder":14,"id":134,"storyBookParagraphs":[]},{"image":{"id":482},"sortOrder":15,"id":135,"storyBookParagraphs":[]},{"image":{"id":483},"sortOrder":16,"id":136,"storyBookParagraphs":[]},{"image":{"id":484},"sortOrder":17,"id":137,"storyBookParagraphs":[]},{"image":{"id":485},"sortOrder":18,"id":138,"storyBookParagraphs":[]},{"image":{"id":486},"sortOrder":19,"id":139,"storyBookParagraphs":[]},{"image":{"id":487},"sortOrder":20,"id":140,"storyBookParagraphs":[]},{"image":{"id":488},"sortOrder":21,"id":141,"storyBookParagraphs":[]},{"image":{"id":489},"sortOrder":22,"id":142,"storyBookParagraphs":[]},{"image":{"id":490},"sortOrder":23,"id":143,"storyBookParagraphs":[]},{"image":{"id":491},"sortOrder":24,"id":144,"storyBookParagraphs":[]},{"image":{"id":492},"sortOrder":25,"id":145,"storyBookParagraphs":[]},{"image":{"id":493},"sortOrder":26,"id":146,"storyBookParagraphs":[]}]

    # Extract the number of paragraphs
    paragraph_count = chapters_utils.get_paragraph_count(chapters_json)

    assert paragraph_count == 0

def test_get_paragraph_count_when_single_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":447},"sortOrder":0,"id":99,"storyBookParagraphs":[{"originalText":"Earth is the planet that we live on. Currently no other planet is known to contain life.","sortOrder":0,"id":142}]},{"image":{"id":448},"sortOrder":1,"id":100,"storyBookParagraphs":[{"originalText":"The Earth is in danger because of global warming. Global warming is caused by too much carbon dioxide in the atmosphere. Carbon dioxide is a gas which traps heat in the Earth. Without it Earth\'s heat would flow out and Earth would freeze.","sortOrder":0,"id":143}]},{"image":{"id":449},"sortOrder":2,"id":101,"storyBookParagraphs":[{"originalText":"The cars we drive create lots of carbon dioxide. We should walk more or ride a bicycle.","sortOrder":0,"id":144}]}]

    # Extract the number of paragraphs
    paragraph_count = chapters_utils.get_paragraph_count(chapters_json)

    assert paragraph_count == 3

def test_get_paragraph_count_when_multiple_paragraphs():
    # Load JSON
    chapters_json = [{"image":{"id":529},"sortOrder":0,"id":180,"storyBookParagraphs":[{"originalText":"One day, in a sleepy village with no electricity, the Electricity Department decided to put up electricity poles.","sortOrder":0,"id":219},{"originalText":"The villagers were excited.","sortOrder":1,"id":220}]},{"image":{"id":530},"sortOrder":1,"id":181,"storyBookParagraphs":[{"originalText":"Every day, a big pit was dug out for each pole.","sortOrder":0,"id":221},{"originalText":"The entire village would gather and watch.","sortOrder":1,"id":222}]},{"image":{"id":531},"sortOrder":2,"id":182,"storyBookParagraphs":[{"originalText":"Ropes were used to pull up the poles. The villagers helped lift the poles into the pits.","sortOrder":0,"id":223},{"originalText":"Even the kids pulled the ropes with all their might. \"HAYYIIISHHHHAAAAAA!\"","sortOrder":1,"id":224}]},{"image":{"id":532},"sortOrder":3,"id":183,"storyBookParagraphs":[{"originalText":"Once the poles were up, the Electricity Department team vanished.","sortOrder":0,"id":225},{"originalText":"Every day, the villagers would wait for them to come back and finish their work. All they could talk about was how excited they were to get electricity.","sortOrder":1,"id":226}]},{"image":{"id":533},"sortOrder":4,"id":184,"storyBookParagraphs":[]},{"image":{"id":534},"sortOrder":5,"id":185,"storyBookParagraphs":[{"originalText":"The villagers began climbing up the poles. The poles gave them a perfect view of their surroundings and far away villages.","sortOrder":0,"id":227},{"originalText":"Days passed, with no sign of the Electricity Department team.","sortOrder":1,"id":229}]},{"image":{"id":535},"sortOrder":6,"id":186,"storyBookParagraphs":[{"originalText":"One evening, a little child took a lantern from her house.","sortOrder":0,"id":231},{"originalText":"She climbed up one of the poles and hung the lantern on top.","sortOrder":1,"id":232}]},{"image":{"id":536},"sortOrder":7,"id":187,"storyBookParagraphs":[{"originalText":"Everyone noticed the lovely bright lantern on top of the pole.","sortOrder":0,"id":233}]},{"image":{"id":537},"sortOrder":8,"id":188,"storyBookParagraphs":[]},{"image":{"id":538},"sortOrder":9,"id":189,"storyBookParagraphs":[{"originalText":"The next evening, the villagers hung lanterns from all five poles.","sortOrder":0,"id":234},{"originalText":"Every day, lanterns were taken down, refueled, and hung back up again.","sortOrder":1,"id":235},{"originalText":"The villagers made a game of it and had lots of fun.","sortOrder":2,"id":236}]},{"image":{"id":539},"sortOrder":10,"id":190,"storyBookParagraphs":[{"originalText":"Then, even without electricity, the nearby villages could spot this little village from afar at night.","sortOrder":0,"id":237},{"originalText":"They began calling it \"The Village of Five Poles.\"","sortOrder":1,"id":240}]},{"image":{"id":540},"sortOrder":11,"id":191,"storyBookParagraphs":[]}]

    # Extract the number of paragraphs
    paragraph_count = chapters_utils.get_paragraph_count(chapters_json)

    assert paragraph_count == 18
