/**
 * Created by Sunny on 4/28/2016.
 */
$(function(){
    $("#previous").click(function (){
	    var page=parseInt(this.title);
		this.href += "&previous="+ page;
	});

	$("#next").click(function(){
		var page = parseInt(this.title);
		this.href += "&next="+page;
	});
});

function AjaxPost(url,data,func,unreload,myInfo){
    if(myInfo){
        $("#"+myInfo).empty();
        $("#"+myInfo).hide();
    }
    var aj = $.ajax({
        type: "POST",
        url: url,
        data: data,
        datatype: "json",
        async: true, //是否异步
        cache: false,
        success: function (datas) {
            if (datas["ret"]=='success') {
                if(func){
                    func(datas["data"])
                }
                if(!unreload){
                    location.reload();
                }
                if(myInfo){
                    $("#"+myInfo).empty()
                    $("#"+myInfo).append(datas["data"]["alert"]);
                    $("#"+myInfo).show();
                }
            } else {
                if(myInfo){
                    $("#"+myInfo).append(datas["forUser"]);
                    $("#"+myInfo).show();
                }else{
                    alert(datas["forUser"]);
                }
            }
        },
        error: function () {
            alert('异常');
        }
    });
}



function ImgHandle(obj,maxImgFileSize,width,height){
    var view = obj.getAttribute("view");
    var msg = obj.getAttribute("msg");
    $("#"+msg).empty();
    if($("#"+msg).is(":visible")){
        $("#"+msg).hide();
    }
    //判断格式
    var str = obj.value.match(/.+.jpg|jpeg|png/i);
    if (str == null) {
        $("#"+msg).append('请选择jpg、png或jpeg格式的图片上传');
        $("#"+msg).show();
        return false;
    }
    if (obj.files[0]) {
        $('#' + view).empty();
        //判断大小
        var fileSize = (obj.files[0].size/1024/1024);
        if (fileSize < maxImgFileSize){
            var reader = new FileReader();
            reader.onload = function (e) {
                //base64img.value = e.target.result;
                //$('#' + view).append("<img src='" + e.target.result +
                //    "'width="+width+"px height="+height+"px " +
                //     "value=" + e.target.result + "/>");
                var obj= document.getElementById(view);
                obj.src = e.target.result;
                obj.setAttribute('value',e.target.result);
            };
            reader.readAsDataURL(obj.files[0]);

        }else{
            $("#"+msg).append('图片大小过大，请重新上传');
            $("#"+msg).show();
            return false;
        }
    }
}


//只允许输入数字
function prevent(e) {
    e.preventDefault ? e.preventDefault() : e.returnValue = false;
}

function digitInput(el, e) {
    var ee = e || window.event; // FF、Chrome IE下获取事件对象
    var c = e.charCode || e.keyCode; //FF、Chrome IE下获取键盘码
    var val = el.val();
    if (c == 110 || c == 190){ // 110 (190) - 小(主)键盘上的点
        (val.indexOf(".") >= 0 || !val.length) && prevent(e); // 已有小数点或者文本框为空，不允许输入点
    } else {
        if ((c != 8 && c != 46 && // 8 - Backspace, 46 - Delete
            (c < 37 || c > 40) && // 37 (38) (39) (40) - Left (Up) (Right) (Down) Arrow
            (c < 48 || c > 57) && // 48~57 - 主键盘上的0~9
            (c < 96 || c > 105)) // 96~105 - 小键盘的0~9
            || e.shiftKey) { // Shift键，对应的code为16
            prevent(e); // 阻止事件传播到keypress
        }
    }
}

//检测手机号码
function CheckPhone(tel){
    var regMobile = /^0?1[3|4|5|8][0-9]\d{8}$/;//手机
    var regTel = /^0[\d]{2,3}-[\d]{7,8}$/; //台式电话
    var regTel2 = /^[\d]{10}$/; //台式电话
    var str = tel.match(regMobile);
    if (str == null) {
        str = tel.match(regTel);
        if (str == null) {
            str = tel.match(regTel2);
            if (str == null) {
                return false;
            }
        }
    }
    return true;
}

function ExcelHandle(obj){
    $("#p_show").hide();
    $("#p_show2").hide();
    $("#p_show").empty();
    $("#p_show2").empty();
    $("#uploadButton").hide();
    var str = obj.value.match(/.+.xls|xlsx/i);
    if (str == null) {
        $("#p_show").append('请选择excel文件上传');
        $("#p_show").show();
        return false;
    }
    $("#p_show2").append('文件路径：'+obj.value);
    $("#p_show2").show();
    $("#uploadButton").show();
}

function ApkHandle(obj){
    $("#p_show").hide();
    $("#p_show2").hide();
    $("#p_show").empty();
    $("#p_show2").empty();
    $("#uploadButton").hide();
    var str = obj.value.match(/.+.apk/i);
    if (str == null) {
        $("#p_show").append('请选择apk文件上传');
        $("#p_show").show();
        return false;
    }
    $("#p_show2").append('文件路径：'+obj.value);
    $("#p_show2").show();
    $("#uploadButton").show();
}

function MyForms(){
    //$("MySubmit").click();
    return false;
}