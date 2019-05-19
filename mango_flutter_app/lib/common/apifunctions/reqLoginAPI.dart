import 'dart:async';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:mango_flutter_app/ui/home_page.dart';
import 'package:mango_flutter_app/common/functions/saveCurrentLogin.dart';
import 'package:mango_flutter_app/common/functions/showDialogSingleButton.dart';
import 'dart:convert';

import 'package:mango_flutter_app/models/json/loginModel.dart';

Future<LoginModel> reqLoginAPI(BuildContext context,
    String username, String password) async {
  final url = "https://mango-api-heroku.herokuapp.com/api/external/login";

  Map<String, String> body = {
    'username' : username,
    'password' : password
  };

  final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: json.encode(body));
  print(body);

  if (response.statusCode == 200){
    final responseJson = json.decode(response.body);
    var user = new LoginModel.fromJson(responseJson);

    saveCurrentLogin(responseJson);
    Navigator.of(context).pushReplacementNamed(HomePage.tag);

    return LoginModel.fromJson(responseJson);
  } else {
    final responseJson = json.decode(response.body);
    print(responseJson);

    saveCurrentLogin(responseJson);
    showDialogSingleButton(context, "Login Failed",
        "Authentication failed. Please try again or contact tech support", "OK");

    return null;
  }
}