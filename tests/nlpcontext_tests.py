from program_synthesis_engine.modules.nlp_context import NlpContext
from program_synthesis_engine.modules.helpers import dump_object
import uuid


sample_texts = \
    [
        u'This is a test sentence',
        u"Add two numbers and get it's sum",
        u"A name uniquley identifies a person. Find all person whose name starts with 'S'",
        u'Who is Tom Cruse ?',
        u'Who is Steve Richards ?',
        u'Who is Ramanujam ?',
        u"Find all users who are above average height.",
        u"This is a tree. What is this? ",
        u"This is a tall tree.",
        u"This is a coconut tree",
        u"This is Tom Cruse"
    ]

contexts = map(lambda x: NlpContext(x), sample_texts)

for context in contexts:
    print "----------------------------------------------------------------"
    print "CONTEXT: {}".format(context.phrase)
    for ent in context.named_entities:
        print ent, ent.label_, ent.start, ent.end
    print "****************************************************************"
    print context.print_tree_on_console()
    print "----------------------------------------------------------------"
    print ""
    print ""

html_gen_code = contexts[0].get_html_visualization_of_trees(contexts[1:])
guid = uuid.uuid4()
with open('Html_visual_{}.html'.format(guid), 'w') as f:
    print "Generating the file with html visualization. Filename: Html_visual_{}.html".format(guid)
    f.write(html_gen_code)
