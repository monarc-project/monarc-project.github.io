Title: Contact us
Slug: contact

<div class="col-md-12">
    <p>Please <a class="contact-us" href="#" data-subject="Monarc question" data-body="Dear NC3 team,

{Please describe your question(s) here.}">contact us</a> in case of any questions related to the MONARC tool use or provided services.</p>
</div>

<div>&nbsp;</div>
<div>&nbsp;</div>

### NC3 contacts

You can also find contact details of National Luxembourg National Cybersecurity Competence Center (NC3) on [the following page](https://nc3.lu/pages/contact.html){:target="_blank"}.

<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      $('.contact-us').click(function() {
        const subject = encodeURIComponent($(this).data('subject'));
        const body = encodeURIComponent($(this).data('body'));

        window.location.href = "mailto:info-monarc@nc3.lu?subject=" + subject + "&body=" + body;
      });
    });
</script>
