from flask import Flask, render_template,request
import predict

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            babyage = request.form.get("babyage")
            ZONE = request.form.get("ZONE")
            enroll_type2 = request.form.get("enroll_type2")
            enroll_age = request.form.get("enroll_age")
            open_rate0 = request.form.get("open_rate0")
            click_rate0 = request.form.get("click_rate0")
            breastfed = request.form.get("breastfed")
            formula = request.form.get("formula")
            breastfed_and_formula = request.form.get("breastfed_and_formula")
            neither = request.form.get("neither")
            redem_rate0 = request.form.get("redem_rate0")
            model = request.form.get("model")

            result = predict.predict( 
                babyage, 
                ZONE, 
                enroll_type2,
                enroll_age,
                open_rate0,
                click_rate0,
                breastfed,
                formula,
                breastfed_and_formula,
                neither,
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