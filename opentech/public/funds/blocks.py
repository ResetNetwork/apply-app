from wagtail.wagtailcore.blocks import StaticBlock

from opentech.public.utils.blocks import StoryBlock


class ProjectsBlock(StaticBlock):
    class Meta:
        icon = 'grip'
        label = 'List of Projects funded'
        template = 'public_funds/blocks/related_projects.html'


class ReviewersBlock(StaticBlock):
    class Meta:
        icon = 'grip'
        label = 'List of fund Reviewers'
        template = 'public_funds/blocks/related_reviewers.html'


class FundBlock(StoryBlock):
    project_list = ProjectsBlock()
    reviewer_list = ReviewersBlock()
