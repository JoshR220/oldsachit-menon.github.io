# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1539732190.4071693
_enable_loop = True
_template_filename = '/home/sm568/.virtualenvs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_title', 'html_translations', 'html_post_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" class="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        def html_translations(post):
            return render_html_translations(context,post)
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        _link = context.get('_link', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_title():
            return render_html_title(context)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
        if author_pages_generated:
            __M_writer('                    <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('                    ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            </span></p>\n            <p class="dateline">\n            <a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time>\n')
        if post.updated and post.updated != post.date:
            __M_writer('                <span class="updated"> (')
            __M_writer(str(messages("updated")))
            __M_writer('\n                    <time class="updated dt-updated" datetime="')
            __M_writer(str(post.formatted_updated('webiso')))
            __M_writer('" itemprop="dateUpdated" title="')
            __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
            __M_writer('</time>)</span>\n')
        __M_writer('            </a>\n            </p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('                    <p class="linkline"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_header.tmpl", "source_encoding": "utf-8", "filename": "/home/sm568/.virtualenvs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_header.tmpl", "line_map": {"23": 3, "26": 2, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 60, "45": 24, "52": 24, "53": 25, "54": 26, "55": 26, "56": 26, "57": 26, "58": 26, "64": 5, "70": 5, "71": 6, "72": 7, "73": 7, "74": 7, "75": 7, "76": 7, "82": 11, "91": 11, "92": 12, "93": 13, "94": 14, "95": 14, "96": 15, "97": 16, "98": 17, "99": 17, "100": 17, "101": 17, "102": 17, "103": 17, "104": 17, "105": 20, "111": 30, "128": 30, "129": 32, "130": 32, "131": 35, "132": 36, "133": 36, "134": 36, "135": 36, "136": 36, "137": 37, "138": 38, "139": 38, "140": 38, "141": 40, "142": 42, "143": 42, "144": 43, "145": 43, "146": 43, "147": 43, "148": 43, "149": 43, "150": 44, "151": 45, "152": 45, "153": 45, "154": 46, "155": 46, "156": 46, "157": 46, "158": 46, "159": 46, "160": 48, "161": 50, "162": 51, "163": 51, "164": 51, "165": 53, "166": 53, "167": 53, "168": 54, "169": 55, "170": 55, "171": 55, "172": 55, "173": 55, "174": 57, "175": 58, "176": 58, "182": 176}}
__M_END_METADATA
"""