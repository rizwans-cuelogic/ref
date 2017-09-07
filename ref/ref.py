"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import String,Scope, Integer
from xblock.fragment import Fragment
from .utils import loader
from xblockutils.studio_editable import StudioEditableXBlockMixin

@XBlock.needs("i18n")
class RefXBlock(StudioEditableXBlockMixin,XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
    reference_name = String(display_name = "Reference Name",default=None,Scope=Scope.content)
    reference_type = String(display_name = "Reference Type",default=None,Scope=Scope.content )
    reference_link = String(display_name = "Reference Link",default=None,Scope=Scope.content)
    reference_description = String(display_name = "Reference Description",multiline_editor=True,default=None,Scope=Scope.content)
    reference_status = String(display_name = "Reference Status",default=None,Scope=Scope.content)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # # TO-DO: change this view to display your data your own way.
    # def student_view(self, context=None):
    #     """
    #     The primary view of the RefXBlock, shown to students
    #     when viewing courses.
    #     """
    #     html = self.resource_string("static/html/ref.html")
    #     frag = Fragment(html.format(self=self))
    #     frag.add_css(self.resource_string("static/css/ref.css"))
    #     frag.add_javascript(self.resource_string("static/js/src/ref.js"))
    #     frag.initialize_js('RefXBlock')
    #     return frag

    # def student_view(self,context=None):
    #     context = {
    #         'reference_name': self.reference_name,
    #         'reference_description': self.reference_description,
    #         'reference_status': self.reference_status,
    #         'reference_link': self.reference_link,
    #         'reference_type':self.reference_type
    #     }
    #     fragment = Fragment()
    #     fragment.add_content(loader.render_template('/static/html/reference_list.html', context))
    #     # fragment.add_css_url(self.runtime.local_resource_url(self, 'public/css/image_explorer.css'))
    #     # fragment.add_javascript(self.resource_string("static/js/src/ref.js"))        
    #     return fragment        

    def student_view(self, context=None):
        """
        Editing view in Studio
        """
        context = {
            'reference_name': self.reference_name,
            'reference_description': self.reference_description,
            'reference_status': self.reference_status,
            'reference_link': self.reference_link,
            'reference_type':self.reference_type
        }
        fragment = Fragment()
        fragment.add_content(loader.render_template('/static/html/reference_create.html', context))
        fragment.add_css(self.resource_string("static/css/ref.css"))
        fragment.add_javascript(self.resource_string("static/js/src/ref.js"))
        fragment.initialize_js('RefXBlock')
        return fragment

    @XBlock.json_handler
    def create_reference(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in..
        self.reference_name=data['data']['reference_name']
        self.reference_type=data['data']['reference_type']
        self.reference_description=data['data']['reference_description']
        self.reference_link=data['data']['reference_link']
        self.reference_status=data['data']['reference_status']
        return {"success": "success"}

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("RefXBlock",
             """<ref/>
             """),
            ("Multiple RefXBlock",
             """<vertical_demo>
                <ref/>
                <ref/>
                <ref/>
                </vertical_demo>
             """),
        ]
