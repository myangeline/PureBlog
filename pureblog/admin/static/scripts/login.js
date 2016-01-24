/**
 * Created by sunshine on 2016/1/12.
 */

var Login = function () {
    var handleLogin = function () {

        $('.login-form').validate({
            errorElement: 'span', //default input error message container
            errorClass: 'help-block', // default input error message class
            focusInvalid: false, // do not focus the last invalid input
            rules: {
                username: {
                    required: true
                },
                password: {
                    required: true
                },
                remember: {
                    required: false
                }
            },

            invalidHandler: function (event, validator) {
                $('.login-error').text("请输入用户名和密码.");
                $('.alert-danger', $('.login-form')).show();
            },

            highlight: function (element) {
                $(element).closest('.form-group').addClass('has-error');
            },

            success: function (label) {
                label.closest('.form-group').removeClass('has-error');
                label.remove();
            },

            errorPlacement: function (error, element) {
                //error.insertAfter(element);
            },

            submitHandler: function (form) {
                Common.ajaxPost(Website.login, $(form).serializeArray(), function (data) {
                    if (data.code === 0) {
                        location.href = data.data;
                    } else {
                        $('.login-error').text(data.error);
                        $('.alert-danger', $('.login-form')).show();
                    }
                });
            }
        });

        $('.login-form input').keypress(function (e) {
            if (e.which == 13) {
                if ($('.login-form').validate().form()) {
                    $('.login-form').submit(); //form validation success, call ajax form submit
                }
                return false;
            }
        });
    };

    var handleForgetPassword = function () {
        $('.forget-form').validate({
            errorElement: 'span', //default input error message container
            errorClass: 'help-block', // default input error message class
            focusInvalid: false, // do not focus the last invalid input
            ignore: "",
            rules: {
                email: {
                    required: true,
                    email: true
                }
            },

            messages: {
                email: {
                    required: "Email不可为空.",
                    email: 'Email地址格式错误'
                }
            },

            invalidHandler: function (event, validator) {

            },

            highlight: function (element) {
                $(element).closest('.form-group').addClass('has-error');
            },

            success: function (label) {
                label.closest('.form-group').removeClass('has-error');
                label.remove();
            },

            errorPlacement: function (error, element) {
                error.insertAfter(element);
            },

            submitHandler: function (form) {
                form.submit();
            }
        });

        $('.forget-form input').keypress(function (e) {
            if (e.which == 13) {
                if ($('.forget-form').validate().form()) {
                    $('.forget-form').submit();
                }
                return false;
            }
        });

        jQuery('#forget-password').click(function () {
            jQuery('.login-form').hide();
            jQuery('.forget-form').show();
        });

        jQuery('#back-btn').click(function () {
            jQuery('.login-form').show();
            jQuery('.forget-form').hide();
        });

    };

    var handleRegister = function () {
        $('.register-form').validate({
            errorElement: 'span',
            errorClass: 'help-block',
            focusInvalid: false,
            ignore: "",
            rules: {
                fullname: {
                    required: true
                },
                email: {
                    required: true,
                    email: true
                },
                address: {
                    required: true
                },

                username: {
                    required: true
                },
                password: {
                    required: true
                },
                rpassword: {
                    equalTo: "#register_password"
                },

                tnc: {
                    required: true
                }
            },

            messages: {
                fullname: {
                    required: "姓名不可为空."
                },
                email: {
                    required: "Email不可为空",
                    email: 'Email地址格式错误'
                },
                address: {
                    required: "地址不可为空"
                },
                username: {
                    required: "用户名不可为空"
                },
                password: {
                    required: "密码不可为空"
                },
                rpassword: {
                    required: "密码不可为空",
                    equalTo: "两次密码不一致"
                },
                tnc: {
                    required: "需要先同意协议."
                }
            },

            invalidHandler: function (event, validator) {

            },

            highlight: function (element) {
                $(element)
                    .closest('.form-group').addClass('has-error');
            },

            success: function (label) {
                label.closest('.form-group').removeClass('has-error');
                label.remove();
            },

            errorPlacement: function (error, element) {
                if (element.attr("name") == "tnc") {
                    error.insertAfter($('#register_tnc_error'));
                } else if (element.closest('.input-icon').size() === 1) {
                    error.insertAfter(element.closest('.input-icon'));
                } else {
                    error.insertAfter(element);
                }
            },

            submitHandler: function (form) {
                $('#register-submit-btn').addClass('disabled');
                Common.ajaxPost(Website.register, $(form).serializeArray(), function (data) {
                    $('#register-submit-btn').removeClass('disabled');
                    if (data.code === 0) {
                        location.href = data.data;
                    } else {
                        if (data.code === 30006){
                            $("#username").after('<span id="username-error" class="help-block">用户名已存在</span>');
                            $("#username").closest('.form-group').addClass('has-error');
                        }
                        Common.notify('error', '注册失败', '');
                    }
                });
            }
        });

        $('.register-form input').keypress(function (e) {
            if (e.which == 13) {
                if ($('.register-form').validate().form()) {
                    $('.register-form').submit();
                }
                return false;
            }
        });

        jQuery('#register-btn').click(function () {
            jQuery('.login-form').hide();
            jQuery('.register-form').show();
        });

        jQuery('#register-back-btn').click(function () {
            jQuery('.login-form').show();
            jQuery('.register-form').hide();
        });
    };

    return {
        init: function () {
            handleLogin();
            handleForgetPassword();
            handleRegister();
        }
    };
}();