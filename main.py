from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_api_request(self):
        Auth = "RwFOkQpJ5yJV_fflc6sMePKJeKKxwT46fwS23adSMQs" 

        headers = {"Auth": Auth}

        payload = {
      
    "email": "aalvarez@enerclic.es",
    "pass": "Lucatoni23"

        }

        response = self.client.post("https://api.users.centro.control.energyccm.com/auth/login", headers=headers, json=payload)

        # Imprime información sobre la respuesta para verificar
        print(f"Respuesta: {response.status_code}, Contenido: {response.text}")
