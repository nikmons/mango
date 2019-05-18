using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mango_InternalClient.Models
{
    public class LoginModel
    {
        public string username;
        public string password;
    }

    public class LoginModelResp
    {
        public string message;
        public string ext_user;
        public string ext_user_id;
        public string access_token;
        public string refresh_token;
    }
}
