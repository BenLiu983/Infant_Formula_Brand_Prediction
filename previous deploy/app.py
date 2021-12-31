from flask import Flask, render_template,request
import predict

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            first_buy_brand = request.form.get("first_buy_brand")
            babyage = request.form.get("babyage")
            ZONE = request.form.get("ZONE")
            breastfeed = request.form.get("breastfeed")
            enroll_type2 = request.form.get("enroll_type2")
            enroll_age = request.form.get("enroll_age")
            open_rate0 = request.form.get("open_rate0")
            click_rate0 = request.form.get("click_rate0")
            redem_rate0 = request.form.get("redem_rate0")

            model = request.form.get("model")

            result = predict.predict(
                first_buy_brand, 
                babyage, 
                ZONE, 
                breastfeed, 
                enroll_type2,
                enroll_age,
                open_rate0,
                click_rate0,
                redem_rate0,
                model
            )
            
            if result == 1:
                message = "This consumer is probably using our brand!"
            else:
                message= "This consumer is not likely using our brand!"
            return render_template("index.html", data = [{"msg":message}])
    except:
        return "Please check if values are entered correctly"
    return render_template("index.html")


if __name__ == "__main__":
    app.run()