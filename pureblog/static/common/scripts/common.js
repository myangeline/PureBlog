/**
 * Created by sunshine on 2016/1/12.
 */

var Common = {
    notify: function (type, message, title) {
        toastr.options = {
            "closeButton": true,
            "debug": false,
            "positionClass": "toast-top-center",
            "onclick": null,
            "showDuration": "1000",
            "hideDuration": "1000",
            "timeOut": "3000",
            "extendedTimeOut": "1000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut"
        };
        toastr[type](message, title)
    },
    ajaxPost: function(url, args, func){
        $.post(url, args, func, 'json');
    },
    ajaxGet: function(url, args, func){
        $.get(url, args, func, 'json');
    }
};

var Website = {
    login: "/admin/login",
    register: '/admin/register',
    upload_file: '/admin/posts/upload'
};