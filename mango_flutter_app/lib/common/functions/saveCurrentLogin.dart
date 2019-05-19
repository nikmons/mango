import 'package:shared_preferences/shared_preferences.dart';
import 'package:mango_flutter_app/models/json/loginModel.dart';

saveCurrentLogin(Map responseJson) async {
  SharedPreferences preferences = await SharedPreferences.getInstance();

  var user;
  if ((responseJson != null && responseJson.isNotEmpty)) {
    user = LoginModel.fromJson(responseJson).ext_user;
  } else {
    user = "";
  }

  var access_token = (responseJson != null && responseJson.isNotEmpty)
      ? LoginModel.fromJson(responseJson).access_token : "";
  var refresh_token = (responseJson != null && responseJson.isNotEmpty)
      ? LoginModel.fromJson(responseJson).refresh_token : "";
  var ext_user_id = (responseJson != null && responseJson.isNotEmpty)
      ? LoginModel.fromJson(responseJson).ext_user_id : 0;

  await preferences.setString('LastUser',
      (user != null && user.length > 0) ? user : "");
  await preferences.setString('LastAccessToken',
      (access_token != null && access_token.length > 0) ? access_token : "");
  await preferences.setString('LastRefreshToken',
      (refresh_token != null && refresh_token.length > 0) ? refresh_token : "");
  await preferences.setInt('LastUserId',
      (ext_user_id != null && ext_user_id > 0) ? ext_user_id : 0);
}