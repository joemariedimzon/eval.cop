from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from eval.cop import MessageFactory as _


# Interface class; used to define content-type schema.

class ICOPDiscussion(form.Schema, IImageScaleTraversable):
    """
    COP Discussion
    """

    title = schema.TextLine(
           title=_(u"Title"),
           required=True,
        )

    dexteritytextindexer.searchable('body')
    form.widget(body=WysiwygFieldWidget)
    body = schema.Text(title=u"Body")


    pass

alsoProvides(ICOPDiscussion, IFormFieldProvider)
