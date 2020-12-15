// SECTION OPENING
const comments_header = $('.comments-header')[0];

function toggleOpenContentComments(header) {
    const comment_header = $(header);
    const arrow = comment_header.find(".caret-icon-fa");
    const comment_content = comment_header.next();

    if (arrow.hasClass('open')) {
        comment_content.removeClass('displayBlock');
        comment_content.addClass('displayNone');
        arrow.removeClass('fa-caret-up');
        arrow.addClass('fa-caret-down');
        arrow.removeClass('open');
    } else {
        comment_content.removeClass('displayNone');
        comment_content.addClass('displayBlock');
        arrow.removeClass('fa-caret-down');
        arrow.addClass('fa-caret-up');
        arrow.addClass('open');
    }
}
