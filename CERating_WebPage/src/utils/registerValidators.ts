import { ref, reactive } from "vue";

export const registerForm = reactive({
    username: "",
    email: "",
    password: "",
    checkpassword: "",
});

// 校验输入内容
const validateCheckPassword = (rule: any, value: string, callback: any) => {
    if (value !== registerForm.password) {
        callback(new Error("Two inputs don't match!"));
    } else {
        callback();
    }
};
export const rulesRegister = ref({
    username: [
        {
            required: true,
            message: "Username could not be empty!",
            trigger: "blur",
        },
        {
            min: 1,
            max: 30,
            message: "Username's length has to be 1 to 30 characters!",
            trigger: "blur",
        },
    ],
    email: [
        {
            type: "email",
            message: "Email is incorrect!",
            required: true,
            trigger: "blur",
        },
    ],
    password: [
        {
            required: true,
            message: "Password could not be empty!",
            trigger: "blur",
        },
        {
            min: 6,
            max: 30,
            message: "Password's length has to be 6 to 30 characters!",
            trigger: "blur",
        },
    ],
    checkpassword: [
        {
            required: true,
            message: "Password could not be empty!",
            trigger: "blur",
        },
        { validator: validateCheckPassword, trigger: "blur" },
    ],
});