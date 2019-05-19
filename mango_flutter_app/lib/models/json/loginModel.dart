class LoginModel {
  final String message;
  final String ext_user;
  final int ext_user_id;
  final String access_token;
  final String refresh_token;

  LoginModel(this.message, this.ext_user, this.ext_user_id,
      this.access_token, this.refresh_token);

  LoginModel.fromJson(Map<String, dynamic> json) :
    message = json['message'],
    ext_user = json['ext_user'],
    ext_user_id = json['ext_user_id'],
    access_token = json['access_token'],
    refresh_token = json['refresh_token'];

  Map<String, dynamic> toJson() =>
      {
        'message' : message,
        'ext_user' : ext_user,
        'ext_user_id' : ext_user_id,
        'access_token' : access_token,
        'refresh_token' : refresh_token
      };
}