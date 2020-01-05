/**
 * Form Password Meter
 */
$(function () {
    "use strict";

    let options = {};

    options.ui = {
        container: "#pwd-container",
        showVerdictsInsideProgressBar: true,
        viewports: {
            progress: ".pwstrength_viewport_progress"
        },
        verdicts: [
            "<i class='fas fa-thumbs-down fa-1x'></i> Weak",
            "<i class='fas fa-flag fa-1x'></i> Normal",
            "<i class='fas fa-leaf fa-1x'></i> Medium",
            "<i class='fas fa-fire fa-1x'></i> Strong",
            "<i class='fas fa-thumbs-up fa-1x'></i> Very Strong"
        ]
    };

    options.rules = {
        raisePower: 1.0
    };

    options.common = {
        minChar: 5,
        debug: false
    };

    let password = $('#id_password, #id_password1, #id_new_password1');

    let progress = $('div.pwstrength_viewport_progress');

    password.pwstrength(options);

    progress.hide();

    password.on('keypress', function () {
        progress.show();
    });
});