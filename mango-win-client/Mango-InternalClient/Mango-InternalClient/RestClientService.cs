using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using Mango_InternalClient.Models;
using Newtonsoft.Json;

namespace Mango_InternalClient
{
    public class RestClientService : IDisposable
    {
        public const string BASE_URL = "http://127.0.0.1:5000/api/external";

        public RestClientService()
        {
            // Log
        }

        public void Dispose()
        {
            
        }

        public HttpResponseMessage PostLogin(string username, string password)
        {
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri(BASE_URL + "/" + "login");
                var content = new StringContent(
                    JsonConvert.SerializeObject(
                        new LoginModel { username = username, password = password }
                        ), Encoding.UTF8, "application/json");
                //httpClient.DefaultRequestHeaders.Add(RequestConstants.UserAgent, RequestConstants.UserAgentValue);

                HttpResponseMessage response = client.PostAsync(BASE_URL + "/" + "login", content).Result;
                //response.EnsureSuccessStatusCode();

                return response;
            }
        }
    }
}
