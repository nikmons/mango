using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Mango_InternalClient.Models;
using Newtonsoft.Json;

namespace Mango_InternalClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnLogin_Click(object sender, RoutedEventArgs e)
        {
            // Call RestClientService.PostLogin
            using (RestClientService restClient = new RestClientService())
            {
                LoginModelResp loginResp;
                try
                {
                    HttpResponseMessage resp = restClient.PostLogin(txtboxUsername.Text, pwboxPassword.Password);

                    if (resp.IsSuccessStatusCode)
                    {
                        string responseBody = resp.Content.ReadAsStringAsync().Result;
                        loginResp = JsonConvert.DeserializeObject<LoginModelResp>(responseBody);

                        if (loginResp != null && loginResp.message == "user_authenticated")
                        {
                            Properties.Settings.Default.access_token = loginResp.access_token;
                            Properties.Settings.Default.refresh_token = loginResp.refresh_token;
                            Properties.Settings.Default.ext_user_id = loginResp.ext_user_id;
                            Properties.Settings.Default.Save();

                            NavigateHome();
                        }
                    }
                    else
                    {
                        var msg= "";
                        switch (resp.ReasonPhrase)
                        {
                            case "UNAUTHORIZED": msg = "Login Failed. Wrong credentials used";
                                    break;
                            default: msg = "Something went wrong";
                                    break;
                        }
                        MessageBox.Show($"{msg}");
                    }
                }
                catch (Exception ex)
                {
                    // 1. Log exception locally
                    // 2. Check if resp code in 4XX                    
                }                                
            }
        }

        private void NavigateHome()
        {
            HomeWindow homeWindow = new HomeWindow();
            homeWindow.Show();
            this.Close();
        }
    }
}
