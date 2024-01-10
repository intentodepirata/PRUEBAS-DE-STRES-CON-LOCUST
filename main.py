from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_api_request(self):
        Auth = "token" 

        headers = {"Auth": Auth}

        payload = {
      
    "email": "correo@correo.es",
    "pass": "PASS"

        }

        response = self.client.post("url", headers=headers, json=payload)

        # Imprime información sobre la respuesta para verificar
        print(f"Respuesta: {response.status_code}, Contenido: {response.text}")
